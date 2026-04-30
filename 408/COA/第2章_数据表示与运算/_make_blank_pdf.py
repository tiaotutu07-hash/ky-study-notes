"""生成模块 2.1 默写空白版 PDF"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
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
            "Q1. 进位计数制的核心规则是什么?",
            "Q2. 「位权」的定义是?",
            "Q3. 二进制 ↔ 八/十六进制 的快速转换方法?",
            "Q4. 十进制 → 任意进制 的方法?(整数 + 小数)",
            "Q5. ASCII 中 '0'、'A'、'a' 的十进制值分别是?",
            "Q6. 大端存储和小端存储的区别?",
            "Q7. 真值和机器数的区别?",
            "Q8. 原码的定义是?",
            "Q9. n+1 位原码整数的范围?",
            "Q10. 补码的定义?",
            "Q11. n+1 位补码整数的范围?它比原码多了什么?",
            "Q12. 补码的「位权法」公式?(零壹独家亮点 ⭐)",
            "Q13. 由 [x]补 求 [-x]补 的方法?",
            "Q14. 变形补码(双符号位 / 模 4 补码)是什么?",
            "Q15. 移码的定义(默认偏置 2^n)?",
            "Q16. 移码与同一真值的补码的关系?",
            "Q17. 移码的「保序性」指什么?为什么浮点阶码用它?",
            "Q18. 四种码各自的实际用途?",
            "Q19. C 语言 int 类型的表示范围?",
            "Q20. C 语言不同字长间整数转换的核心规则?",
        ],
    },
    {
        "category": "二、易错默写(红笔对应)",
        "items": [
            "Q21. ⚠️ 哪几种码对 0 的表示不唯一?",
            "Q22. ⚠️ 为什么十进制 0.3 不能精确转换为二进制?",
            "Q23. ⚠️ 二↔八/十六分组时,补 0 规则?",
            "Q24. ⚠️ 8 位原码能表示的不同数值有多少个?",
            "Q25. ⚠️ 真值 -2^n 在哪几种 n+1 位编码中能表示?",
            "Q26. ⚠️ 8 位补码 1000 0000 对应真值是什么?它的原码呢?",
            "Q27. ⚠️ 移码的偏置量一定是 2^n 吗?",
            "Q28. ⚠️ 求 [-x]移 时什么情况会溢出?",
            "Q29. ⚠️ 同一个 8 位位串 1000 0000 在不同解释下的真值?",
            "Q30. ⚠️ C 语言中 signed 和 unsigned 数混合运算时如何处理?",
            "Q31. ⚠️ 8421 BCD 码加法什么时候需要修正?",
        ],
    },
    {
        "category": "三、跨章关联默写",
        "items": [
            "Q32. 补码「减法变加法」的具体形式是?(→ 2.2 节)",
            "Q33. 双符号位(变形补码)如何判断溢出?(→ 2.2 节)",
            "Q34. 浮点数中尾数和阶码分别用什么编码?(→ 2.3 节)",
            "Q35. 0.3 转二进制不精确这一性质,在浮点数中体现为什么?(→ 2.3 节)",
            "Q36. 大端/小端会在哪些场景中再次出现?(→ 第 4 章 / CN / OS)",
        ],
    },
]

make_blank_pdf(
    "模块 2.1 数制与编码",
    questions,
    r"D:\Desktop\小e专注学习\考研学习\408\COA\第2章_数据表示与运算\模块2_1_默写_空白版.pdf",
)
