from typing import IO


def render(size: int, f: IO) -> None:
    """
    Generates a simple HTML file with a table containing `tableSize` rows.
    """
    f.write("<html>\n")
    f.write("<head><title>Performance Test Document</title></head>\n")
    f.write("<body>\n")
    f.write("<h1>Table Test ({} rows)</h1>\n".format(size))
    f.write("<table border='1'>\n")
    for i in range(size):
        f.write("<tr><td>Row {}</td><td>Some data</td></tr>\n".format(i + 1))
    f.write("</table>\n")
    f.write("</body>\n")
    f.write("</html>\n")
