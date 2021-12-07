class Script:
    """A collection of actions.

    The responsibility of Script is to keep track of a collection of actions. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actions (dict): A dictionary of actions { key: group_name, value: a list of actions }
    """

    def __init__(self):
        """Constructs a new Action."""
        self._current_actions = {}
        self._valid_groups = {"input", "update", "output"}
        # self._removed_actions = {}
        
    def add_action(self, group, action):
        """Adds an action to the given group.
        
        Args:
            group (string): The name of the group. Must be either "input", "update", or "output"
            action (Action): The action to add.
        """
        if group not in self._valid_groups:
            raise ValueError(f"Error: 'group' must be one of the following values: {self._valid_groups}")

        if not group in self._current_actions.keys():
            self._current_actions[group] = []
            
        if not action in self._current_actions[group]:
            self._current_actions[group].append(action)

    def get_actions(self, group):
        """Gets the actions in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The actions in the group.
        """
        results = []
        if group in self._current_actions.keys():
            results = self._current_actions[group].copy()
        return results
    
    def remove_action(self, group, action):
        """Removes an action from the given group.
        
        Args:
            group (string): The name of the group.
            action (Action): The action to remove.
        """
        if group in self._current_actions:
            try:
                self._current_actions[group].remove(action)
            except:
                print(f"Action '{action}' is NOT found in the script")