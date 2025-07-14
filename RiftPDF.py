import os

def split_pdf_with_ghostscript():
    input_pdf = input("Please enter the path of the PDF file to split: ").strip()
    if not os.path.isfile(input_pdf):
        print("File does not exist.")
        return

    try:
        num_parts = int(input("How many parts to split into: ").strip())
        if num_parts < 1:
            print("The number of parts must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    parts_input = input("Please enter the page ranges for each part (comma separated, e.g. 1-3,4-6,7-10): ").strip()
    parts = [p.strip() for p in parts_input.split(',') if p.strip()]
    if len(parts) != num_parts:
        print("The number of entered parts does not match the specified split count.")
        return

    for idx, part in enumerate(parts, 1):
        if '-' in part:
            try:
                start, end = map(int, part.split('-'))
            except Exception:
                print(f"Page range format error in part {idx}.")
                return
        else:
            try:
                start = end = int(part)
            except Exception:
                print(f"Page range format error in part {idx}.")
                return

        output_pdf = f"output_part_{idx}.pdf"
        # Ghostscript command
        gs_cmd = (
            f'gswin64 -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER '
            f'-dFirstPage={start} -dLastPage={end} '
            f'-sOutputFile="{output_pdf}" "{input_pdf}"'
        )
        print(f"Generating: {output_pdf} (Pages: {start}-{end})")
        ret = os.system(gs_cmd)
        if ret != 0:
            print(f"Failed to generate {output_pdf}.")
        else:
            print(f"{output_pdf} generated successfully.")

if __name__ == "__main__":
    split_pdf_with_ghostscript()
