import pytest
from faker import Faker
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status


@pytest.mark.e2e
async def test_create_chat_success(
    app: FastAPI,
    client: AsyncClient,
    faker: Faker,
) -> None:
    url = app.url_path_for("create_chat")
    title = faker.text(max_nb_chars=100)
    response = await client.post(url, json={"title": title})
    json_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert json_data["id"]


@pytest.mark.e2e
async def test_create_chat_fail_the_same_title_already_exists(
    app: FastAPI,
    client: AsyncClient,
    faker: Faker,
) -> None:
    url = app.url_path_for("create_chat")
    title = faker.text(max_nb_chars=100)
    await client.post(url, json={"title": title})
    response = await client.post(url, json={"title": title})
    json_data = response.json()

    assert response.status_code == status.HTTP_400_BAD_REQUEST, json_data
    assert json_data["detail"]["error"], json_data


@pytest.mark.e2e
async def test_create_chat_fail_title_is_too_long(
    app: FastAPI,
    client: AsyncClient,
    faker: Faker,
) -> None:
    url = app.url_path_for("create_chat")
    title = faker.text(max_nb_chars=300)
    response = await client.post(url, json={"title": title})
    json_data = response.json()

    assert response.status_code == status.HTTP_400_BAD_REQUEST, json_data
    assert json_data["detail"]["error"], json_data


@pytest.mark.e2e
async def test_create_chat_fail_title_is_empty(
    app: FastAPI,
    client: AsyncClient,
) -> None:
    url = app.url_path_for("create_chat")
    response = await client.post(url, json={"title": ""})
    json_data = response.json()

    assert response.status_code == status.HTTP_400_BAD_REQUEST, json_data
    assert json_data["detail"]["error"], json_data
