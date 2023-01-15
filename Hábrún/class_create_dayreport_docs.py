from docx import Document

class Docs:

    def __init__(self) -> None:
        pass

    def merge_docs(self, filenames:list):
        pass

    def edit_docs_template(self, pallet_number, owner, dates:list[str], box_weight:list[list], rowsum, total, size, template_filename, new_filename):
        
        # Open the template document
        template_document = Document(template_filename)

        # add data

        # Save the modified document
        template_document.save(new_filename)
        
    def delete_docs(self, filename):
        pass

