class ControllerBase[T]:
    def __init__(self, model: T) -> None:
        self.model = model
        self.views = {}

    def add_view(self, view_name: str, view: T) -> None:
        try:
            if not (view_name in self.views):
                self.views[view_name] = view
            else:
                raise ValueError("View already added!")
        except ValueError as ve:
            print(ve)
