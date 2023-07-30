# ArkDev Content Archive via PDF

A Python3 script to archive multiple pages in CSV file publically available online using Python PDF file printing utiltiy `wasyprint` into a directory on local machine.

## Usage

The first step is to install the latest version of Python from the [Microsoft Store](https://apps.microsoft.com/store/detail/python-38/9MSSZTT1N39L?hl=en-us&gl=us).

When Python is installed, you have to install GTK. Download the latest [GTK3 installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases) and launch it. If you don’t know what some options mean, you can safely keep the default options selected.

General steps for setting up the script on Windows from `cmd`:

```batch
c:\> c:\Python35\python -m venv c:\path\to\myenv
c:\> c:\path\to\myenv\Scripts\activate.bat
c:\> CD c:\path\to\myenv
c:\> pip install weasyprint
```

To run the archiver:
```
c:\> CD c:\path\to\myenv
c:\> Sripts\activate.bat
c:\> python ark_archiver.py <file.CSV default=input.csv> <Output Directoy default=archive_pdfs>
```

### Linux

To activate the `venv` on linux using `bash` and run the script+0:

```bash
$ cd /path/to/project
$ . venv/bin/activate
$ python ark_archiver.py
```

## Input CSV

Input file in the format `csv`, comma separated and columns are string quoted. 

The file must have the following constraints:

* No headers in the first row.
* The first column must be the generated PDF file name that will be adjusted based on OS.
* The second column must be the full URL for content to archive and must be accessible to anonymous users.
* Any more columns will be ignored by the script, but can be useful for documentation purposes. 

## Output PDF

Generated PDFs are created in the **Output Directory**, that will be next to the script. Default name is `archive_pdfs`.
PDF generation can take some time, because each URL must be fetched and rendered based on all CSS rules to generate the correct PDF.

## Resources

* [Python venv installation](https://docs.python.org/3/library/venv.html)
* [Python Usage on Windows](https://docs.python.org/3/using/windows.html#using-on-windows)
* [Weasyprint installation on Windows](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)
