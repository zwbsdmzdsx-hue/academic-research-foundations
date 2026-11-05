"""Plot the synthetic teaching case. Optional dependency: matplotlib.
Run after: python -m pip install matplotlib
All plotted values are recomputed from teaching-measurements.csv.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from analyze import analyze

root = Path(__file__).resolve().parent
result = analyze()
differences = result['differences_g']
fig, (ax, summary) = plt.subplots(1, 2, figsize=(9.2, 5.8),
    gridspec_kw={'width_ratios': [3, 2]}, constrained_layout=True)
colors = ['#235b44' if d < 0 else '#9a3241' if d > 0 else '#526159' for d in differences]
ax.hlines(range(1, 21), 0, differences, color=colors, linewidth=1.4, alpha=.7)
ax.scatter(differences, range(1, 21), c=colors, s=32, zorder=3)
ax.set_yticks(range(1, 21), [f'O{i:02d}' for i in range(1, 21)])
ax.invert_yaxis()
ax.set_title('Every paired object', loc='left', fontsize=12)
ax.set_xlabel('Absolute error difference, B - A (g)')
mean = result['mean_difference_b_minus_a_g']
lo, hi = result['ci95_low_g'], result['ci95_high_g']
summary.errorbar(mean, 0, xerr=[[mean-lo], [hi-mean]], fmt='o',
    capsize=7, color='#235b44', markersize=8, linewidth=2)
summary.set_yticks([])
summary.set_ylim(-.8, .8)
summary.set_title('Mean and model-based 95% CI', loc='left', fontsize=12)
summary.set_xlabel('Mean difference (g)')
summary.text(.5, .24, f'Mean = {mean:.3f} g\n95% CI [{lo:.3f}, {hi:.3f}] g\nn = 20 paired objects',
    transform=summary.transAxes, ha='center', va='top', fontsize=10, linespacing=1.8)
for axis in (ax, summary):
    axis.axvline(0, color='#526159', linestyle='--', linewidth=1)
    axis.set_xlim(-2.25, .75)
    axis.grid(axis='x', color='#d3dcd3', linewidth=.6)
    axis.set_axisbelow(True)
    axis.spines[['top','right']].set_visible(False)
fig.suptitle('Synthetic teaching data: not experimental evidence', fontsize=14, color='#24352e')
fig.savefig(root/'paired-differences.svg', format='svg', metadata={'Date':None})
fig.savefig(root/'paired-differences.png', dpi=160)
print('Wrote paired-differences.svg and paired-differences.png')
