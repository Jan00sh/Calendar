# Calendar

Calendar Web App created using Python by PyLearn Discord Team.

## Requirements

Git
Python 3.6+

### Installation

Clone repository to create a local copy on your computer and move to created folder:
```sh
git clone https://github.com/PyLearn-Team/Calendar.git
cd Calendar
```
Make sure that you have virtualenv installed:
```sh
pip install virtualenv
```
Create a virtual environment:
```sh
virtualenv env
```
Activate virtual environment:
```sh
source env/bin/activate
```
Install all dependencies:
```sh
pip install -r requirements.txt
```

### Running

Run a local server using a following command:
```sh
uvicorn main:app --reload
```
Navigate to localhost:8000 in your browser.

## Contributing
If you want to help us doing our projects check out our [website](https://pylearn-team.github.io/) for more informations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
