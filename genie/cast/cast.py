class Cast:
    """A collection of actors.

    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._current_actors = {}
        # self._removed_actors = {}
        
    def add_actor(self, group, actor):
        """Adds an actor to the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to add.
        """
        if not group in self._current_actors.keys():
            self._current_actors[group] = []
            
        if not actor in self._current_actors[group]:
            self._current_actors[group].append(actor)

    def get_actors(self, group):
        """Gets the actors in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The actors in the group.
        """
        results = []
        if group in self._current_actors.keys():
            results = self._current_actors[group].copy()
        return results
    
    def get_all_actors(self):
        """Gets all of the actors in the cast.
        
        Returns:
            List: All of the actors in the cast.
        """
        results = []
        for group in self._current_actors:
            results.extend(self._current_actors[group])
        return results

    def get_first_actor(self, group):
        """Gets the first actor in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first actor in the group.
        """
        result = None
        if group in self._current_actors.keys() and len(self._current_actors[group]) > 0:
            result = self._current_actors[group][0]
        return result

    def remove_actor(self, group, actor):
        """
            Simply add the actor to the removed_actors dictionary.
            The removed_actors dictionary has the same {"group": [elements...]} structure
                as the current_actor dictionary, but it only contains actors to be removed
        """
        if group in self._current_actors.keys():
            try:
                self._current_actors[group].remove(actor)
            except:
                print(f"Actor '{actor}' are NOT found in the cast")
        # if not group in self._removed_actors:
        #     self._removed_actors[group] = []

        # if not actor in self._removed_actors[group]:
        #     self._removed_actors[group].append(actor)
    
    # def apply_changes(self):
    #     """
    #         Look at all the groups and actors in removed_actors, delete the
    #         corresponding actors in current_actors
    #     """
    #     # Look at all the group that has actors to be deleted specified in removed_actors
    #     for group in self._removed_actors:
    #         if group in self._current_actors.keys():
    #             for actor in self._removed_actors[group]:
    #                 try:
    #                     self._current_actors[group].remove(actor)
    #                 except:
    #                     print(f"WARNING: '{actor}' is specified in removed_actors but NOT found in current_actors. Skipping to other actors to delete...")
        
    #     # Clear the removed_actors dict to get ready for the next iteration
    #     self._removed_actors.clear()