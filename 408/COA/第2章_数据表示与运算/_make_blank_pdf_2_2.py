"""生成模块 2.2 默写空白版 PDF"""
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
            "Q1. 一位全加器(FA)的接口是?",
            "Q2. FA 的逻辑表达式是?",
            "Q3. 串行进位加法器和并行进位加法器(CLA)的延迟差异?",
            "Q4. 并行进位的核心思想?(G_i / P_i 函数)",
            "Q5. OF 标志位的计算公式与作用?",
            "Q6. CF 标志位的计算公式与作用?",
            "Q7. SF 标志位的定义与作用?",
            "Q8. ZF 标志位的定义?",
            "Q9. ALU 的接口?",
            "Q10. 逻辑移位的规则?",
            "Q11. 算术左移的规则与溢出条件?",
            "Q12. 算术右移的规则与精度丢失?",
            "Q13. ROL/ROR 与 RCL/RCR 的区别?",
            "Q14. 补码加减运算的核心公式?",
            "Q15. 补码运算的 4 个特点?",
            "Q16. 溢出判断法 1(单符号位)?",
            "Q17. 溢出判断法 2(双符号位)?",
            "Q18. 溢出判断法 3(进位异或)?",
            "Q19. 加减运算电路如何用一套加法器同时支持加和减?",
            "Q20. 无符号大小比较看哪些标志位?",
            "Q21. 有符号大小比较看哪些标志位?",
            "Q22. 原码一位乘法的两个步骤?",
            "Q23. Booth 比较法的 4 种操作?",
            "Q24. 乘法运算电路的关键寄存器?",
            "Q25. 补码除法(加减交替)的核心规则?",
        ],
    },
    {
        "category": "二、易错默写(红笔对应)",
        "items": [
            "Q26. ⚠️ 减法运算时 CF 公式有什么特殊?",
            "Q27. ⚠️ 为什么 OF 在无符号运算下无意义?",
            "Q28. ⚠️ 同样,CF 在有符号运算下为什么无意义?",
            "Q29. ⚠️ 什么情况下加减运算一定不会溢出?",
            "Q30. ⚠️ 双符号位补码中,哪一位才是结果的真符号位?",
            "Q31. ⚠️ 加减运算电路硬件能否区分有符号 vs 无符号?",
            "Q32. ⚠️ 有符号比较时,为什么不能光看 SF 判正负?",
            "Q33. ⚠️ 原码乘法过程中的右移是哪种移位?",
            "Q34. ⚠️ 无符号乘法溢出判断的具体规则?",
            "Q35. ⚠️ 有符号乘法溢出判断的具体规则?",
            "Q36. ⚠️ 32 位 int 整数除法,什么情况下会发生溢出?",
            "Q37. ⚠️ 整数除法时除数为 0 会怎样?",
            "Q38. ⚠️ 不恢复余数法和恢复余数法的区别?",
            "Q39. ⚠️ 无符号数的算术右移和逻辑右移结果是否一样?",
        ],
    },
    {
        "category": "三、跨章关联默写",
        "items": [
            "Q40. ALU 在 CPU 数据通路中的位置?(→ 第 5 章)",
            "Q41. OF/CF/SF/ZF 在指令系统中如何被使用?(→ 第 5 章)",
            "Q42. 补码加减为什么「减法变加法」?(→ 2.1 节)",
            "Q43. 除数为 0 异常如何被 CPU 处理?(→ 第 5 章)",
            "Q44. 位级等价性在浮点编码中如何体现?(→ 2.3 节)",
        ],
    },
]

make_blank_pdf(
    "模块 2.2 运算方法和运算电路",
    questions,
    r"D:\Desktop\小e专注学习\考研学习\408\COA\第2章_数据表示与运算\模块2_2_默写_空白版.pdf",
)
