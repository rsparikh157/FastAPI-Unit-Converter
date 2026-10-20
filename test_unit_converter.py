from codebase import calc, unit_converter
from fastapi.testclient import TestClient
import pytest

client = TestClient(unit_converter)


def test_km_to_m():
    assert calc("km", "m", 5) == 5000.0


def test_kg_to_g():
    assert calc("kg", "g", 5) == 5000.0

def test_convert_endpoint():
    response = client.get(
        "/convert",
        params={
            "value": 5,
            "from_unit": "km",
            "to_unit": "m"
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 5000.0


def test_temperature_endpoint():
    response = client.get(
        "/convert",
        params={
            "value": 68,
            "from_unit": "fahrenheit",
            "to_unit": "celsius"
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 20.0


def test_incompatible_units_endpoint():
    response = client.get(
        "/convert",
        params={
            "value": 5,
            "from_unit": "km",
            "to_unit": "kg"
        }
    )

    assert response.status_code == 400


def test_invalid_unit_endpoint():
    response = client.get(
        "/convert",
        params={
            "value": 5,
            "from_unit": "xyz",
            "to_unit": "m"
        }
    )

    assert response.status_code == 422

def test_to_unit():
    response = client.get(
        "/convert",
        params={
            "value": 5,
            "from_unit": "km",
        }
    )
    assert response.status_code == 422

def test_invlaid_to_unit():
    response = client.get(
        "/convert",
        params={
            "value": 5,
            "from_unit": "km",
            "to_unit": "xyz"
        }
    )

    assert response.status_code == 422

def test_zero_value():
    response = client.get(
        "/convert",
        params={
            "value": 0,
            "from_unit": "km",
            "to_unit": "m"
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 0.0


def test_negative_value():
    response = client.get(
        "/convert",
        params={
            "value": -5,
            "from_unit": "km",
            "to_unit": "m"
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == -5000.0

def test_valid_decimal():
    response = client.get(
            "/convert",
            params={
                "value": 2.5,
                "from_unit": "km",
                "to_unit": "m"
            }
        )

    assert response.status_code == 200
    assert response.json()["result"] == 2500.0

def test_non_numeric():
    response = client.get(
            "/convert",
            params={
                "value": "abc",
                "from_unit": "km",
                "to_unit": "m"
            }
        )

    assert response.status_code == 422
    assert "detail" in response.json()

def test_same_unit():
    response = client.get(
            "/convert",
            params={
                "value": 5,
                "from_unit": "km",
                "to_unit": "km"
            }
        )

    assert response.status_code == 200
    assert response.json()["result"] == 5.0

def test_mb_to_kb():
    response = client.get(
                "/convert",
                params={
                    "value": 5,
                    "from_unit": "MB",
                    "to_unit": "kB"
                }
            )
    assert response.status_code == 200
    assert response.json()["result"] == 5000.0

def test_mib_to_kib():
    response = client.get(
                "/convert",
                params={
                    "value": 5,
                    "from_unit": "MiB",
                    "to_unit": "KiB"
                }
            )
    assert response.status_code == 200
    assert response.json()["result"] == 5120.0

def test_k_to_c():
    response = client.get(
                "/convert",
                params={
                    "value": 300,
                    "from_unit": "kelvin",
                    "to_unit": "celsius"
                }
            )
    assert response.status_code == 200
    assert response.json()["result"] == pytest.approx(26.85)


def test_c_to_f():
    response = client.get(
                "/convert",
                params={
                    "value": 25,
                    "from_unit": "celsius",
                    "to_unit": "fahrenheit"
                }
            )
    assert response.status_code == 200
    assert response.json()["result"] == 77.00