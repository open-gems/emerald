import opendataloader_pdf


opendataloader_pdf.convert(
    input_path=["input/input.pdf"],
    output_dir="output/",
    image_output="off",
    html_page_separator="%page-number%",
    format="html",
)