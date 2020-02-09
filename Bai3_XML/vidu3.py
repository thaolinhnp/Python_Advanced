from xml.dom.minidom import Document
import xml.dom.minidom
import os.path

def make_xml(path):
    if (os.path.isfile(path)):
        doc = xml.dom.minidom.parse(path)
        root_xml = doc.documentElement
    else:
        doc = Document()
        root_xml = doc.createElement('books')
        doc.appendChild(root_xml)

    child_node = doc.createElement('book')
    noi_dung = 'Đường xa con hát'
    child_node.setAttribute('title',noi_dung)
    root_xml.appendChild(child_node)

    author = doc.createElement('author')
    tac_gia = 'Đỗ Nhật Nam'
    author.appendChild(doc.createTextNode(tac_gia))
    child_node.appendChild(author)
    return doc

if __name__ == "__main__":
    make_xml('files_xml/book.xml').writexml(open(file='files_xml/book.xml', mode='w', encoding='utf8'),indent='',addindent='',newl='')