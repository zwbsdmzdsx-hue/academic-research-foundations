# 实证定量教学材料

所有20行数据均为人工构造，仅用于学习；不是实际实验结果，也不是用户完成的科研成果。

## 文件

- teaching-measurements.csv：20个对象，每个有A、B配对读数。
- analyze.py：Python 3标准库分析，无需安装第三方依赖。
- analysis-results.json：分析脚本输出。
- case-facts.json：全教材共同采用的定义、结果与解释边界。
- spreadsheet-guide.md：表格软件从导入到计算与图表的步骤。
- data-dictionary.csv：每列的定义和有效条件。

## 从零运行 Python

1. 安装Python 3。在Windows安装时选择将Python加入PATH。若已安装，在终端输入 `python --version` 检查；某些设备用 `python3 --version`。
2. 将 `analyze.py` 和 `teaching-measurements.csv` 保存到同一文件夹。脚本以自身位置找CSV，文件名不要改。
3. 在该文件夹打开终端，输入 `python analyze.py`，macOS/Linux若命令为python3则用 `python3 analyze.py`。
4. 终端会显示结果，并在同一文件夹生成 `analysis-results.json`。最先核对n=20、mean_difference_b_minus_a_g=-0.75。
5. 若提示找不到CSV，检查文件是否被保存成 `.csv.txt`，以及是否与脚本在同一目录。若提示PermissionError，将材料放到可写目录后运行。
6. 不要把运行成功等同方法适用。请返回教材核对独立单位、配对关系、测量过程与模型假设。

## 计算边界

这份无依赖脚本用不完全Beta函数计算t分布尾概率，用二分法求临界值；它便于离线教学，不是替代经过长期验证的统计软件。结果已由独立SciPy的配对差t分析和置信区间核对。真实研究可用R或SciPy等工具，并保留版本、输入和诊断。

原始数据没有缺失，没有真实抽样或随机化；不得从构造数据宣称某现实流程有效。真实参考值还可能有校准不确定性。

## 可选：重新绘图

统计分析脚本不需要第三方库。图形已随HTML嵌入，可直接下载SVG。若要重绘，在CSV、analyze.py、make_figure.py同一文件夹中，先运行 `python -m pip install matplotlib`，再运行 `python make_figure.py`。脚本从CSV重算数据，生成SVG和PNG。左图为20个对象的差值，右图的误差条是均值的95%模型区间，不是标准差或原始值范围。
