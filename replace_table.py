 def replace_table(self,old_text,new_text):
        for table in self.doc.tables:
    	    for row in table.rows:
                for cell in row.cells:
                    if old_text in cell.text:
                        print(cell.text)
                        text = cell.paragraphs[0].runs[0].text.replace(old_text,new_text)
                        cell.paragraphs[0].runs[0].text = text
                        print(text)
