from api.BoardApi import BoardApi
import allure

def test_create_board(api_client: BoardApi, delete_board: dict, test_data:dict):
    org_id = test_data("org_id")
    board_list_before = api_client.get_all_boards_by_org_id(org_id)

    resp = api_client.creat_board("New board to be delete")   
    delete_board["board_id"] = resp.get("id")

    board_list_after = api_client.get_all_boards_by_org_id(org_id)

    with allure.step("Проверить, что количество досок стало больше на 1"):
        assert len(board_list_after) - len(board_list_before) == 1

def test_delete_board(api_client: BoardApi, dummy_board_id: str, test_data:dict):
    org_id = test_data("org_id")
    board_list_before = api_client.get_all_boards_by_org_id(org_id)

    api_client.delete_board_by_id(dummy_board_id)

    board_list_after = api_client.get_all_boards_by_org_id(org_id)

    with allure.step("Проверить, что количество досок стало меньше на 1"):
        assert len(board_list_before) - len(board_list_after) == 1
