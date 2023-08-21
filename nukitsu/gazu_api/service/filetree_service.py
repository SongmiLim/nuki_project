class FileTreeService:

    def __init__(self, view):
        super().__init__()
        self.view = view

        if not self.view.filetree.isSortingEnabled():
            self.view.filetree.setSortingEnabled(True)  # 할당된 순서대로 표시 후 헤더 누르면 오름차순 정렬
