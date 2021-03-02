## Steps

```sh
docker-compose run --rm python bash
pip install -r requirements.txt
pytest test_repro.py --junitxml="result.xml"
```

## What happens

`result.xml` will have `file="mock_decorator.py"`

## What did I expect

`file` attribute should be `test_repro.py` instead of `mock_decorator.py`
