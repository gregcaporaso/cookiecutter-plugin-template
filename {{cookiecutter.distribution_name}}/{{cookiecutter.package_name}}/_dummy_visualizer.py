# This file is only included as an example. Remove this file when you are
# ready to develop your plugin.
import os
import os.path

import pandas as pd


def mapping_viz(output_dir: str, mapping1: dict, mapping2: dict,
                key_label: str, value_label: str) -> None:
    df1 = _dict_to_dataframe(mapping1, key_label, value_label)
    df2 = _dict_to_dataframe(mapping2, key_label, value_label)

    with open(os.path.join(output_dir, 'index.html'), 'w') as fh:
        fh.write('<html><head>')
        fh.write('<link rel="stylesheet" type="text/css" '
                 'href="css/style.css" />')
        fh.write('</head>\n')
        fh.write('<body>\n')
        fh.write('<h3>mapping1:</h3>\n')
        fh.write(df1.to_html(index=False, classes='dummy-class'))
        fh.write('<h3>mapping2:</h3>\n')
        fh.write(df2.to_html(index=False, classes='dummy-class'))
        fh.write('</body></html>')

    css_dir = os.path.join(output_dir, 'css')
    os.mkdir(css_dir)
    with open(os.path.join(css_dir, 'style.css'), 'w') as fh:
        fh.write(_css)


def _dict_to_dataframe(dict_, key_label, value_label):
    return pd.DataFrame(sorted(dict_.items()),
                        columns=[key_label, value_label])


# Example table styling taken from http://www.w3schools.com/css/css_table.asp
_css = """
.dummy-class {
    border-collapse: collapse;
    width: 100%;
}

.dummy-class th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
"""
