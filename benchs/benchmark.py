#!/usr/bin/env python3

import os
import psutil
import subprocess
import time
import matplotlib.pyplot as plt


def generateDocumentSimple(tableSize: int, out: str) -> None:
    """
    Generates a simple HTML file with a table containing `tableSize` rows.
    """
    with open(out, "w") as f:
        f.write("<html>\n")
        f.write("<head><title>Performance Test Document</title></head>\n")
        f.write("<body>\n")
        f.write("<h1>Table Test ({} rows)</h1>\n".format(tableSize))
        f.write("<table border='1'>\n")
        for i in range(tableSize):
            f.write("<tr><td>Row {}</td><td>Some data</td></tr>\n".format(i + 1))
        f.write("</table>\n")
        f.write("</body>\n")
        f.write("</html>\n")


def generateDoculentLedger(tableSize: int, out: str) -> None:
    """
    Generates a simple HTML file with a table containing `tableSize` rows.
    """

    tableSize = tableSize // 100
    with open(out, "w") as f:
        f.write("""
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <link type="text/css" rel="stylesheet" href="general-ledger.css"/>
</head>

<body dir="ltr">
<div class="o_content ">
    <header>
        <div class="o_title">
            General Ledger
        </div>
        <div class="row o_header_font">
            <div class="col-8">

                <div class="row">
                    <div class="col-10">YourCompany</div>
                </div>

                <address class="mb-0 o_text_muted">
                    <address class="o_portal_address mb-0" itemscope="itemscope"
                             itemtype="http://schema.org/Organization">
                        <div class="gap-2" itemprop="address" itemscope="itemscope"
                             itemtype="http://schema.org/PostalAddress">
                            <div class="d-flex align-items-baseline gap-1">
                                    <span class="d-block w-100 lh-sm" itemprop="streetAddress">250 Executive Park Blvd,
                                        Suite 3400<br/>San Francisco CA 94134<br/>United States</span>
                            </div>
                        </div>
                    </address>
                </address>

                <span class="o_text_muted">
                        VAT:US12345671
                    </span>
            </div>
            <div class="col-4">


                <div class="row" name="filter_info_template_journals">
                </div>


                <div class="row" name="pdf_options_header">
                    <div class="col-9 o_text_muted">


                    </div>
                </div>
            </div>
        </div>
    </header>

    <div class="align-items-start">
        <table class="o_table  ">

            <thead id="table_header">
            <tr>

                <th></th>


                <th colspan="6">
                    Feb 2024
                </th>

            </tr>

            <tr>

                <th></th>

                <th>Invoice Date</th>
                <th>Communication</th>
                <th>Partner</th>
                <th>Debit</th>
                <th>Credit</th>
                <th>Balance</th>
            </tr>
            </thead>


            <tbody>
""")

        for i in range(tableSize):
            f.write("""


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    101401 Bank
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 12,477.45</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 32.58</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 12,444.87</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    Initial Balance
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 6,378.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 6,378.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    MISC/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 2,500.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 8,878.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Bank Fees</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 32.58</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 8,845.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00005
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">First $ 2,000.00 of invoice 2024/00001</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 2,000.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,495.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00006
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Last Year Interests</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 102.78</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,598.20</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00007
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">INV/2024/00002</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 12,348.20</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00008
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">R:9772938 10/07 AX 9415116318 T:5 BRT: 100.00 C/ croip</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 96.67</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 12,444.87</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    101402 Bank Suspense Account
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 32.58</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,977.45</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -9,944.87</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    Initial Balance
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 6,378.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -6,378.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Bank Fees</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 32.58</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -6,345.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -6,995.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00005
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">First $ 2,000.00 of invoice 2024/00001</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 2,000.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -8,995.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00006
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Last Year Interests</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 102.78</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -9,098.20</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00007
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">INV/2024/00002</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -9,848.20</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00008
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">R:9772938 10/07 AX 9415116318 T:5 BRT: 100.00 C/ croip</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 96.67</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -9,944.87</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    121000 Account Receivable
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 145,675.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 145,675.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    Initial Balance
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 36,512.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -36,512.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    MISC/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 2,500.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -39,012.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    MISC/2024/02/0002
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 2,500.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -36,512.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">INV/2024/00001</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 36,512.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/06/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">INV/2024/00004</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 36,512.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 36,512.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/11/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 36,512.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/18/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">INV/2024/00003</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 22,137.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 22,137.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00002
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">INV/2024/00002</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 48,012.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 70,150.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00005
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 22,137.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 48,012.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/20/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 48,012.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    131000 Tax Paid
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 85.67</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 85.67</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    Initial Balance
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 81.17</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 81.17</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BILL/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">15%</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 4.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 4.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RBILL/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">15%</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 4.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    211000 Account Payable
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 656.77</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 656.77</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    Initial Balance
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 622.27</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 622.27</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BILL/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 34.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -34.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RBILL/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 34.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    251000 Tax Received
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 18,675.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 18,675.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    Initial Balance
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 4,762.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 4,762.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">15%</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 4,762.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/06/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">15%</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 4,762.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -4,762.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/11/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">15%</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 4,762.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/18/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">15%</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 2,887.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -2,887.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00002
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">15%</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 6,262.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -9,150.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00005
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">15%</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 2,887.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -6,262.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/20/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">15%</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 6,262.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    400000 Product Sales
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 124,500.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 127,000.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -2,500.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    Initial Balance
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 31,750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 31,750.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    MISC/2024/02/0002
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 2,500.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 29,250.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class="">[FURN_6741] Large Meeting Table
                                Conference room table</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 20,000.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,250.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8220] Four Person Desk
                                Four person modern office workstation</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -2,500.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/06/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class="">[FURN_6741] Large Meeting Table
                                Conference room table</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 20,000.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -22,500.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/06/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8220] Four Person Desk
                                Four person modern office workstation</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -34,250.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/11/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class="">[FURN_6741] Large Meeting Table
                                Conference room table</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 20,000.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -14,250.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/11/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8220] Four Person Desk
                                Four person modern office workstation</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -2,500.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/18/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8999] Three-Seat Sofa
                                Three Seater Sofa with Lounger in Steel Grey Colour</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 7,500.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -10,000.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/18/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8220] Four Person Desk
                                Four person modern office workstation</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -21,750.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00002
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8220] Four Person Desk
                                Four person modern office workstation</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -33,500.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00002
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8999] Three-Seat Sofa
                                Three Seater Sofa with Lounger in Steel Grey Colour</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 30,000.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -63,500.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00005
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8999] Three-Seat Sofa
                                Three Seater Sofa with Lounger in Steel Grey Colour</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 7,500.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -56,000.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00005
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8220] Four Person Desk
                                Four person modern office workstation</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -44,250.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/20/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8220] Four Person Desk
                                Four person modern office workstation</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -32,500.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/20/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8999] Three-Seat Sofa
                                Three Seater Sofa with Lounger in Steel Grey Colour</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 30,000.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -2,500.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    600000 Expenses
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 30.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 30.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BILL/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">[FURN_7777] Office Chair</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 10.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 10.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BILL/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">[FURN_9999] Office Design Software</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 20.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 30.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RBILL/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">[FURN_7777] Office Chair</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 10.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 20.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RBILL/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">[FURN_9999] Office Design Software</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 20.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1">
                <td class="o_line_name_level" colspan="1">
                    999999 Undistributed Profits/Losses
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 541.10</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 541.10</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    Total
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 302,673.57</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 302,673.57</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    101401 Bank
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 12,477.45</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 32.58</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 12,444.87</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    Initial Balance
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 6,378.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 6,378.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    MISC/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 2,500.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 8,878.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Bank Fees</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 32.58</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 8,845.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>
            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,495.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00005
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">First $ 2,000.00 of invoice 2024/00001</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 2,000.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,495.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00006
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Last Year Interests</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 102.78</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,598.20</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00007
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">INV/2024/00002</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 12,348.20</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00008
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">R:9772938 10/07 AX 9415116318 T:5 BRT: 100.00 C/ croip</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 96.67</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 12,444.87</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    101402 Bank Suspense Account
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 32.58</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 9,977.45</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -9,944.87</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    Initial Balance
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 6,378.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -6,378.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Bank Fees</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 32.58</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -6,345.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Prepayment</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 650.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -6,995.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00005
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">First $ 2,000.00 of invoice 2024/00001</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 2,000.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -8,995.42</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00006
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Last Year Interests</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 102.78</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -9,098.20</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00007
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">INV/2024/00002</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -9,848.20</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BNK1/2024/00008
                </td>

                <td class="o_cell_td">

                    <span class="">02/21/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">R:9772938 10/07 AX 9415116318 T:5 BRT: 100.00 C/ croip</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 96.67</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -9,944.87</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    121000 Account Receivable
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 145,675.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 145,675.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    Initial Balance
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 36,512.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -36,512.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    MISC/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 2,500.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -39,012.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    MISC/2024/02/0002
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 2,500.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -36,512.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">INV/2024/00001</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 36,512.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/06/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">INV/2024/00004</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 36,512.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 36,512.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/11/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 36,512.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/18/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">INV/2024/00003</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 22,137.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 22,137.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00002
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">INV/2024/00002</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 48,012.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 70,150.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00005
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 22,137.50</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 48,012.50</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/11/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class="">[FURN_6741] Large Meeting Table
                                Conference room table</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 20,000.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -14,250.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/11/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8220] Four Person Desk
                                Four person modern office workstation</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -2,500.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/18/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8999] Three-Seat Sofa
                                Three Seater Sofa with Lounger in Steel Grey Colour</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 7,500.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -10,000.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00003
                </td>

                <td class="o_cell_td">

                    <span class="">02/18/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8220] Four Person Desk
                                Four person modern office workstation</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -21,750.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00002
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8220] Four Person Desk
                                Four person modern office workstation</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -33,500.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    INV/2024/00002
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8999] Three-Seat Sofa
                                Three Seater Sofa with Lounger in Steel Grey Colour</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 30,000.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -63,500.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00005
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8999] Three-Seat Sofa
                                Three Seater Sofa with Lounger in Steel Grey Colour</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 7,500.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -56,000.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00005
                </td>

                <td class="o_cell_td">

                    <span class="">02/19/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8220] Four Person Desk
                                Four person modern office workstation</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -44,250.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/20/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8220] Four Person Desk
                                Four person modern office workstation</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 11,750.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -32,500.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RINV/2024/00004
                </td>

                <td class="o_cell_td">

                    <span class="">02/20/2024</span>
                </td>
                <td class="o_cell_td">

                            <span class=" o_overflow_value">[FURN_8999] Three-Seat Sofa
                                Three Seater Sofa with Lounger in Steel Grey Colour</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Deco Addict</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 30,000.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ -2,500.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    600000 Expenses
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 30.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 30.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BILL/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">[FURN_7777] Office Chair</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 10.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 10.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    BILL/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">[FURN_9999] Office Design Software</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 20.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 30.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RBILL/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">[FURN_7777] Office Chair</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 10.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 20.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_3">
                <td class="o_line_name_level" colspan="1">
                    RBILL/2024/02/0001
                </td>

                <td class="o_cell_td">

                    <span class="">02/01/2024</span>
                </td>
                <td class="o_cell_td">

                    <span class="">[FURN_9999] Office Design Software</span>
                </td>
                <td class="o_cell_td">

                    <span class="">Azure Interior</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 20.00</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1">
                <td class="o_line_name_level" colspan="1">
                    999999 Undistributed Profits/Losses
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 541.10</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 541.10</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    Total
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 302,673.57</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 302,673.57</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number o_muted">$ 0.00</span>
                </td>

            </tr>


            <tr name="pdf_export_main_table_body_lines_tr" class="o_line_level_1 o_fw_bold">
                <td class="o_line_name_level" colspan="1">
                    101401 Bank
                </td>

                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class=""></span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 12,477.45</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 32.58</span>
                </td>
                <td class="o_cell_td">

                    <span class="o_line_cell_value_number">$ 12,444.87</span>
                </td>

            </tr>
                    """)

        f.write("""
                            </tbody>
        </table>
    </div>


    <ul class="o_footnote">
    </ul>
</div>
</body>

</html>
                """)


generateDocument = generateDoculentLedger
useLogScale = True


def measure_command_usage(command):
    """
    Spawns a process via psutil, measures the time and peak memory usage.
    It attempts to include child processes in the memory measurement.
    Returns (elapsed_time_in_seconds, peak_memory_in_MB).
    """
    # Start time
    start_time = time.time()

    # Launch process
    process = psutil.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    peak_memory = 0

    # While the process is running, poll memory usage
    while True:
        if process.poll() is not None:
            # The process has finished
            break

        # Get memory usage of the process and all its children
        try:
            mem_info = process.memory_info().rss
            for child in process.children(recursive=True):
                mem_info += child.memory_info().rss
            if mem_info > peak_memory:
                peak_memory = mem_info
        except psutil.NoSuchProcess:
            pass

        time.sleep(0.05)  # Poll at 50ms intervals

    # Final check in case memory peaked right before the loop ended
    try:
        mem_info = process.memory_info().rss
        for child in process.children(recursive=True):
            mem_info += child.memory_info().rss
        if mem_info > peak_memory:
            peak_memory = mem_info
    except psutil.NoSuchProcess:
        pass

    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Convert peak memory from bytes to MB
    peak_memory_mb = peak_memory / (1024.0 * 1024.0)

    return elapsed_time, peak_memory_mb


def main():
    # Powers of 10 up to 1,000,000
    table_sizes = [
        10**i for i in range(1, 5)
    ]  # [10, 100, 1000, 10000, 100000, 1000000]

    pm_times = []
    pm_mems = []
    wk_times = []
    wk_mems = []

    for size in table_sizes:
        html_file = f"test_{size}.html"
        print(f"Generating HTML document with {size} rows...")
        generateDocument(size, html_file)

        # Measure paper-muncher
        pm_cmd = [
            "paper-muncher",
            "print",
            html_file,
            "-o",
            "/dev/null",
            "--scale",
            "0.65x",
        ]
        print(f"Measuring paper-muncher performance for tableSize={size}...")
        t_pm, m_pm = measure_command_usage(pm_cmd)
        pm_times.append(t_pm)
        pm_mems.append(m_pm)

        # Measure wkhtmltopdf
        wk_cmd = ["wkhtmltopdf", "--enable-local-file-access", html_file, "/dev/null"]
        print(f"Measuring wkhtmltopdf performance for tableSize={size}...")
        t_wk, m_wk = measure_command_usage(wk_cmd)
        wk_times.append(t_wk)
        wk_mems.append(m_wk)

        # Clean up HTML file if you want
        os.remove(html_file)

    # --- Plot results ---
    fig, (ax_time, ax_mem) = plt.subplots(1, 2, figsize=(12, 6))

    # Time plot
    ax_time.plot(table_sizes, pm_times, marker="o", label="paper-muncher (time)")
    ax_time.plot(table_sizes, wk_times, marker="o", label="wkhtmltopdf (time)")
    if useLogScale:
        ax_time.set_xscale("log")
        ax_time.set_xlabel("Table Size (log scale)")
    else:
        ax_time.set_xlabel("Table Size")
    ax_time.set_ylabel("Time (seconds)")
    ax_time.set_title("Conversion Time")
    ax_time.legend()
    ax_time.grid(True)

    # Memory plot
    ax_mem.plot(table_sizes, pm_mems, marker="o", label="paper-muncher (memory)")
    ax_mem.plot(table_sizes, wk_mems, marker="o", label="wkhtmltopdf (memory)")
    if useLogScale:
        ax_mem.set_xscale("log")
        ax_mem.set_xlabel("Table Size (log scale)")
    else:
        ax_mem.set_xlabel("Table Size")
    ax_mem.set_ylabel("Peak Memory (MB)")
    ax_mem.set_title("Peak Memory Usage")
    ax_mem.legend()
    ax_mem.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
