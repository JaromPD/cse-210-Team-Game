from cast import Cast

def main():
    cast = Cast()
    cast.add_actor("astroid", "astroid1")
    cast.add_actor("astroid", "astroid2")
    cast.add_actor("astroid", "astroid3")
    cast.add_actor("astroid", "astroid4")

    cast.add_actor("ship", "ship1")

    cast.add_actor("mothership", "mothership1")

    cast.add_actor("bullet", "bullet1")
    cast.add_actor("bullet", "bullet2")
    cast.add_actor("bullet", "bullet3")

    cast.add_actor("score", "score1")

    # Test add_actor and get_actors:
    print("--------- Test add_actor() and get_actors() ---------")
    print(cast.get_actors("astroid"))
    print(cast.get_actors("ship"))
    print(cast.get_actors("mothership"))
    print(cast.get_actors("bullet"))
    print(cast.get_actors("score"))
    print("\n")

    # Test get_all_actors:
    print("--------- Test get_all_actors() ---------")
    print(cast.get_all_actors())
    print("\n")

    # Test get_first_actor:
    print("--------- Test get_first_actors() ---------")
    print(cast.get_first_actor("astroid"))
    print(cast.get_first_actor("bullet"))
    print(cast.get_first_actor("ship"))
    print(cast.get_first_actor("mothership"))
    print(cast.get_first_actor("score"))
    print("\n")

    # Test remove_actor:
    print("--------- Test remove_actor() ---------")
    cast.remove_actor("astroid", "astroid2")
    cast.remove_actor("bullet", "bullet10")
    cast.remove_actor("bullet", "bullet1")
    cast.remove_actor("bullet", "bullet3")
    print(cast._current_actors)
    # print(cast._removed_actors)
    print("\n")

    # Test apply_changes: use the removed_actors dictionary populated
    #  in the above test to delete actors from current_actors:
    # print("--------- Test apply_changes() ---------")
    # cast.apply_changes()
    # print(cast._current_actors)
    # print(cast._removed_actors)
    # print("\n")


if __name__ == "__main__":
    main()