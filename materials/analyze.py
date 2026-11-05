"""Teaching-only paired measurements. Python 3, standard library only.
Run: python analyze.py  (from any directory). No real experimental data.
"""
from pathlib import Path
import csv
import json
import math
import statistics as stats

ROOT = Path(__file__).resolve().parent

def beta_fraction(a, b, x):
    """Continued fraction for the regularized incomplete beta function."""
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1, a - 1
    c = 1.0
    d = 1 - qab * x / qap
    d = 1 / (d if abs(d) > tiny else tiny)
    h = d
    for m in range(1, 300):
        aa = m * (b-m) * x / ((qam+2*m)*(a+2*m))
        d = 1 + aa*d
        d = d if abs(d)>tiny else tiny
        c = 1 + aa/c
        c = c if abs(c)>tiny else tiny
        d = 1/d
        h *= d*c
        aa = -(a+m)*(qab+m)*x/((a+2*m)*(qap+2*m))
        d = 1+aa*d
        d = d if abs(d)>tiny else tiny
        c = 1+aa/c
        c = c if abs(c)>tiny else tiny
        d = 1/d
        change = d*c
        h *= change
        if abs(change-1)<3e-14:
            return h
    raise ArithmeticError('Incomplete beta did not converge')

def regularized_beta(x,a,b):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    front = math.exp(math.lgamma(a+b)-math.lgamma(a)-math.lgamma(b)+a*math.log(x)+b*math.log1p(-x))
    if x < (a+1)/(a+b+2):
        return front*beta_fraction(a,b,x)/a
    return 1-front*beta_fraction(b,a,1-x)/b

def two_sided_t_p(t,df):
    return regularized_beta(df/(df+t*t),df/2,0.5)

def t_critical_975(df):
    low, high=0.0,100.0
    for _ in range(90):
        mid=(low+high)/2
        if two_sided_t_p(mid,df)>0.05: low=mid
        else: high=mid
    return (low+high)/2

def analyze(path=ROOT/'teaching-measurements.csv'):
    with open(path,encoding='utf-8-sig',newline='') as stream:
        rows=list(csv.DictReader(stream))
    if len(rows)!=20 or len({r['object_id'] for r in rows})!=20:
        raise ValueError('This teaching case requires 20 distinct paired objects.')
    a=[abs(float(r['measurement_a_g'])-float(r['reference_g'])) for r in rows]
    b=[abs(float(r['measurement_b_g'])-float(r['reference_g'])) for r in rows]
    if not all(math.isfinite(x) for x in a+b):
        raise ValueError('Measurements and reference values must be finite numbers.')
    d=[y-x for x,y in zip(a,b)]
    n=len(d); mean=stats.mean(d); sd=stats.stdev(d); se=sd/math.sqrt(n)
    if se == 0:
        raise ValueError('All paired differences are identical; the demonstrated t statistic is undefined.')
    t=mean/se; critical=t_critical_975(n-1)
    leave_one_out=[stats.mean(d[:i]+d[i+1:]) for i in range(n)]
    results={'case':'teaching-only-synthetic-paired-measurements','n':n,'df':n-1,
        'mean_abs_error_a_g':stats.mean(a),'mean_abs_error_b_g':stats.mean(b),
        'mean_difference_b_minus_a_g':mean,'sd_difference_g':sd,'se_difference_g':se,
        'ci95_low_g':mean-critical*se,'ci95_high_g':mean+critical*se,
        't':t,'p_two_sided':two_sided_t_p(t,n-1),'t_critical':critical,
        'b_lower_count':sum(x<0 for x in d),'equal_count':sum(x==0 for x in d),
        'b_higher_count':sum(x>0 for x in d),'differences_g':d,
        'median_difference_g':stats.median(d),
        'leave_one_out_mean_min_g':min(leave_one_out),
        'leave_one_out_mean_max_g':max(leave_one_out),
        'warning':'构造的教学模拟数据；统计值仅演示模型计算，不是现实研究结果。'}
    return results

if __name__=='__main__':
    result=analyze()
    (ROOT/'analysis-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))
