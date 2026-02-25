import requests
from api.BoardApi import BoardApi

base_url = "https://trello.com/ru"

def test_create_board(api_client: BoardApi, delete_board: dict):
    board_list_before = api_client.get_all_boards_by_org_id("ID организации")

    resp = api_client.creat_board("New board to be delete")   
    delete_board["board_id"] = resp.get("id")

    board_list_after = api_client.get_all_boards_by_org_id("ID организации")

    assert len(board_list_after) - len(board_list_before) == 1

def test_delete_board(api_client: BoardApi, dummy_board_id: str):
    board_list_before = api_client.get_all_boards_by_org_id("ID организации")

    api_client.delete_board_by_id(dummy_board_id)

    board_list_after = api_client.get_all_boards_by_org_id("ID организации")

    assert len(board_list_before) - len(board_list_after) == 1
