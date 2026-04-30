"""生成模块 2.3 默写空白版 PDF"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))


def make_blank_pdf(module_name, questions, output_path):
    doc = SimpleDocTemplate(
        output_path, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2.5 * cm, bottomMargin=2.5 * cm,
    )

    title_s = ParagraphStyle('T', fontName='STSong-Light', fontSize=20, spaceAfter=20)
    head_s = ParagraphStyle('H', fontName='STSong-Light', fontSize=14,
                            spaceAfter=10, spaceBefore=15, textColor='#1a4480')
    q_s = ParagraphStyle('Q', fontName='STSong-Light', fontSize=11,
                         spaceAfter=80, leading=18)
    meta_s = ParagraphStyle('M', fontName='STSong-Light', fontSize=11,
                            spaceAfter=20)

    story = [
        Paragraph(f"默写测试 · {module_name}", title_s),
        Paragraph("日期:______年___月___日   得分:______/100   用时:______ 分", meta_s),
    ]
    for cat in questions:
        story.append(Paragraph(cat['category'], head_s))
        for q in cat['items']:
            story.append(Paragraph(q, q_s))

    doc.build(story)
    print(f"PDF generated: {output_path}")


questions = [
    {
        "category": "一、概念默写(蓝笔对应)",
        "items": [
            "Q1. 浮点数的通用表达公式?",
            "Q2. 浮点数中尾数和阶码各决定什么?",
            "Q3. 浮点数表示范围数轴上的 4 个不可表示区?",
            "Q4. 浮点数规格化的数学定义(基数为 2)?",
            "Q5. 原码规格化的正/负数尾数形式?",
            "Q6. 补码规格化的正/负数尾数形式?",
            "Q7. 左规和右规的规则与适用场景?",
            "Q8. IEEE 754 单精度浮点数的格式?",
            "Q9. IEEE 754 双精度浮点数的格式?",
            "Q10. IEEE 754 阶码偏置量的公式?",
            "Q11. IEEE 754 的「隐藏位」是什么?",
            "Q12. IEEE 754 阶码全 0、尾数全 0 表示什么?",
            "Q13. IEEE 754 阶码全 0、尾数非 0 表示什么?",
            "Q14. IEEE 754 阶码全 1、尾数全 0 表示什么?",
            "Q15. IEEE 754 阶码全 1、尾数非 0 表示什么?",
            "Q16. float 类型的最大正数和有效十进制位数?",
            "Q17. double 类型的最大正数和有效十进制位数?",
            "Q18. 浮点数加减运算的五个步骤?",
            "Q19. 浮点对阶的规则?",
            "Q20. IEEE 754 的默认舍入方式?",
            "Q21. 浮点运算的真溢出由什么决定?",
            "Q22. 浮点乘除运算的核心公式?",
            "Q23. 浮点乘除步骤与加减的关键差异?",
            "Q24. 大端方式和小端方式的区别?",
            "Q25. struct 边界对齐的两条规则?",
        ],
    },
    {
        "category": "二、易错默写(红笔对应)",
        "items": [
            "Q26. ⚠️ 浮点数发生上溢时的处理?",
            "Q27. ⚠️ 浮点数发生下溢时的处理?",
            "Q28. ⚠️ 右规和左规分别可能引发什么溢出?",
            "Q29. ⚠️ IEEE 754 偏置量为什么不是经典移码的 2^(k-1)?",
            "Q30. ⚠️ 非规格化数的真实指数 E 为什么不是 0 - bias?",
            "Q31. ⚠️ IEEE 754 的隐藏位在哪些数中存在?",
            "Q32. ⚠️ 十进制 0.1 能否精确转二进制?",
            "Q33. ⚠️ 浮点对阶为什么不能「大阶向小阶」看齐?",
            "Q34. ⚠️ 尾数溢出是否一定意味着浮点结果真的溢出?",
            "Q35. ⚠️ 浮点乘除的规格化只需检查一次,加减为什么要多次?",
            "Q36. ⚠️ int 转 float 是否会精度损失?",
            "Q37. ⚠️ float 转 int 时数据如何处理?",
            "Q38. ⚠️ struct 中成员的顺序对 sizeof 的影响?",
            "Q39. ⚠️ Intel x86 是大端还是小端?网络字节序呢?",
        ],
    },
    {
        "category": "三、跨章关联默写",
        "items": [
            "Q40. 浮点数的舍入误差和 2.1 节哪个性质直接相关?(→ 2.1)",
            "Q41. IEEE 754 阶码用移码而不是补码,本质好处是什么?(→ 2.1)",
            "Q42. 大小端和 struct 对齐在主存中如何影响指令执行?(→ 第 4 章)",
            "Q43. 浮点指令在 CPU 中如何处理?(→ 第 5 章)",
        ],
    },
]

make_blank_pdf(
    "模块 2.3 浮点数的表示与运算",
    questions,
    r"D:\Desktop\小e专注学习\考研学习\408\COA\第2章_数据表示与运算\模块2_3_默写_空白版.pdf",
)
