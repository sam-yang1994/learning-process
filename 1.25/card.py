import card_tool


while True:
    card_tool.show_menu()
    action = input('请选择你的操作')
    print('你选择的操作是【%s】' % action)
    if action in ['1', '2', '3']:
        if action == '1':
            card_tool.new_card()
        elif action == '2':
            card_tool.card_show()
        elif action == '3':
            card_tool.card_look()

    elif action == '0':
        print('欢迎再次使用名片系统')
        break
    else:
        print('操作无效，请重新选择')

