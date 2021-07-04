

class Plugins:

    def header(self, data):
        return f"<h{data.level}> {data.text} <h{data.level}/>"

    def list(self, data):
        pass