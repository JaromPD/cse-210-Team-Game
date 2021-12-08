from script import Script

def main():
    script = Script()
    script.add_action("input", "HandleQuitAction")
    script.add_action("input", "HandleShipMovementAction")
    script.add_action("input", "HandleShootingAction")

    script.add_action("update", "SpawnAstroidsCollision")
    script.add_action("update", "HandleShipAstroidsCollision")
    script.add_action("update", "HandleMothershipAstroidsCollision")
    script.add_action("update", "HandleShipOffscreenAction")

    script.add_action("output", "DrawActorsActions")
    script.add_action("output", "UpdateScreenAction")

    # Test add_action and get_actions:
    print("--------- Test add_action() and get_actions() ---------")
    print(script.get_actions("input"))
    print(script.get_actions("update"))
    print(script.get_actions("output"))
    print("\n")

    # Test remove_action:
    print("--------- Test remove_action() ---------")
    script.remove_action("input", "HandleShootingAction")
    script.remove_action("update", "SpawnAstroidsCollision")
    script.remove_action("output", "DrawActorsActions")
    print(script._current_actions)
    # print(script._removed_actions)
    print("\n")

    # Test apply_changes: use the removed_actions dictionary populated
    #  in the above test to delete actors from current_actions:
    # print("--------- Test apply_changes() ---------")
    # script.apply_changes()
    # print(script._current_actions)
    # print(script._removed_actions)
    # print("\n")


if __name__ == "__main__":
    main()