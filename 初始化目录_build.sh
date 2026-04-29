#!/bin/bash
# 任逸考研学习仓库 · 一劳永逸目录初始化脚本
# 用法: bash build.sh

set -e

# 仓库根目录(在脚本里改成你的实际路径)
ROOT="$(pwd)"

echo "🏗️  初始化目录结构 @ $ROOT"
echo ""

# ============= 顶层目录 =============
mkdir -p "$ROOT/.claude/skills"
mkdir -p "$ROOT/_错题清单"
mkdir -p "$ROOT/_打卡"
mkdir -p "$ROOT/_archive"
echo "✅ 顶层目录: .claude/skills, _错题清单, _打卡, _archive"

# ============= 数学 =============
# 高数 1-18 讲(数学一全要)
GS_NAMES=(
  "第1讲_函数极限连续"
  "第2讲_数列极限"
  "第3讲_一元函数微分概念"
  "第4讲_一元函数微分计算"
  "第5讲_微分应用一"
  "第6讲_中值定理"
  "第7讲_微分应用三"
  "第8讲_一元积分概念性质"
  "第9讲_一元积分计算"
  "第10讲_积分应用一"
  "第11讲_积分应用二"
  "第12讲_积分应用三"
  "第13讲_多元微分"
  "第14讲_二重积分"
  "第15讲_微分方程"
  "第16讲_级数"
  "第17讲_多元积分预备"
  "第18讲_多元积分"
)
for ch in "${GS_NAMES[@]}"; do
  mkdir -p "$ROOT/数学/高数/$ch/原材料"
done
echo "✅ 数学/高数:18 讲已建"

# 线代 1-6 讲
XD_NAMES=(
  "第0讲_零基础铺垫"
  "第1讲_行列式"
  "第2讲_矩阵"
  "第3讲_向量"
  "第4讲_线性方程组"
  "第5讲_特征值"
  "第6讲_二次型"
)
for ch in "${XD_NAMES[@]}"; do
  mkdir -p "$ROOT/数学/线代/$ch/原材料"
done
echo "✅ 数学/线代:7 讲已建"

# 概率 8 讲(余丙森,粗略分章,等切 PDF 时再细调)
GL_NAMES=(
  "第1讲_随机事件与概率"
  "第2讲_随机变量及其分布"
  "第3讲_多维随机变量"
  "第4讲_随机变量数字特征"
  "第5讲_大数定律与中心极限定理"
  "第6讲_数理统计基本概念"
  "第7讲_参数估计"
  "第8讲_假设检验"
)
for ch in "${GL_NAMES[@]}"; do
  mkdir -p "$ROOT/数学/概率/$ch/原材料"
done
echo "✅ 数学/概率:8 讲已建"

# 三大计算
mkdir -p "$ROOT/数学/三大计算/不定积分"
mkdir -p "$ROOT/数学/三大计算/定积分"
mkdir -p "$ROOT/数学/三大计算/求导"
echo "✅ 数学/三大计算 已建"

# ============= 408 =============
# DS 8 章
DS_NAMES=(
  "第1章_绪论"
  "第2章_线性表"
  "第3章_栈队列数组"
  "第4章_串"
  "第5章_树与二叉树"
  "第6章_图"
  "第7章_查找"
  "第8章_排序"
)
for ch in "${DS_NAMES[@]}"; do
  mkdir -p "$ROOT/408/DS/$ch/原材料"
done
echo "✅ 408/DS:8 章已建"

# COA 7 章
COA_NAMES=(
  "第1章_概述"
  "第2章_数据表示与运算"
  "第3章_存储系统"
  "第4章_指令系统"
  "第5章_中央处理器"
  "第6章_总线"
  "第7章_输入输出系统"
)
for ch in "${COA_NAMES[@]}"; do
  mkdir -p "$ROOT/408/COA/$ch/原材料"
done
echo "✅ 408/COA:7 章已建"

# OS 章节(王道分 6 章)
OS_NAMES=(
  "第1章_概述"
  "第2章_进程与线程"
  "第3章_内存管理"
  "第4章_文件管理"
  "第5章_输入输出管理"
  "第6章_进程同步与死锁"
)
for ch in "${OS_NAMES[@]}"; do
  mkdir -p "$ROOT/408/OS/$ch/原材料"
done
echo "✅ 408/OS:6 章已建"

# CN 5 章
CN_NAMES=(
  "第1章_计算机网络体系结构"
  "第2章_物理层"
  "第3章_数据链路层"
  "第4章_网络层"
  "第5章_传输层"
  "第6章_应用层"
)
for ch in "${CN_NAMES[@]}"; do
  mkdir -p "$ROOT/408/CN/$ch/原材料"
done
echo "✅ 408/CN:6 章已建"

# DS 大题手册放跨章位置
mkdir -p "$ROOT/408/DS/_大题手册"
echo "✅ 408/DS/_大题手册 已建"

# ============= 英语 =============
mkdir -p "$ROOT/英语/真题精读"
mkdir -p "$ROOT/英语/词典"
mkdir -p "$ROOT/英语/语法"
mkdir -p "$ROOT/英语/单词默写本"
mkdir -p "$ROOT/英语/作文素材"

# 真题精读年份目录(英一为主,2000-2024)
for year in {2000..2024}; do
  for text in 1 2 3 4; do
    mkdir -p "$ROOT/英语/真题精读/${year}_Text${text}/原材料"
  done
done
echo "✅ 英语:真题精读 25年×4篇 已建"

# 跨年共享文件占位
touch "$ROOT/英语/_错题逻辑本.md"
touch "$ROOT/英语/_熟词僻意表.md"
touch "$ROOT/英语/_长难句本.md"
echo "✅ 英语:跨年共享文件已建"

# ============= 政治 =============
mkdir -p "$ROOT/政治"
echo "✅ 政治:占位目录已建(7月后启用)"

# ============= 顶层文件占位 =============
[ ! -f "$ROOT/_PROJECT_README.md" ] && touch "$ROOT/_PROJECT_README.md" && echo "✅ _PROJECT_README.md 占位已建"

echo ""
echo "🎉 全部目录初始化完成"
echo ""
echo "下一步:"
echo "  1. 把 SKILL.md 文件放到 .claude/skills/ 下"
echo "  2. 写 _PROJECT_README.md(用我之前给的模板)"
echo "  3. 切 PDF 到对应 原材料/ 目录"
