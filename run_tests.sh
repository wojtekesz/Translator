CMD=`command -v python3`
if [ "$CMD" != '' ]
then
	PYTHON=python3
fi
CMD=`command -v py`
if [ "$CMD" != '' ]
then
	PYTHON=py
fi

$PYTHON -m unittest discover -s tests -p "unittest*.py"
$PYTHON -m pytest tests/pytest*
$PYTHON -m unittest discover -s tests -p "translatorTest*.py"

