 #replace_paragraph.py
 #replace_paragraph 功能是在docx文件中保持文本格式不变替换相应内容
 def replace_paragraph(old_text,new_text):
        for p in doc.paragraphs:
          if old_text in p.text:
             inline = p.runs
             for i in inline:
                 if old_text in i.text:
                     print(i.text)
                     text = i.text.replace(old_text,new_text)
                     i.text = text
