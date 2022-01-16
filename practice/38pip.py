from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
#google pypi -> search -> copy -> terminal --> and copy 내용