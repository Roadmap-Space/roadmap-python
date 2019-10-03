from . import model


class Subscribers(model.Model):
    def add(self, id, token, sub, cb):
        self.post(
            "/subscribers/" + self.compress_id(id, token),
            sub,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def like(self, id, token, cb):
        self.put(
            "/subscribers/" + self.compress_id(id, token),
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def save(self, id, token, sub, cb):
        self.put(
            "/subscribers/save/" + self.compress_id(id, token),
            sub,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def remove(self, id, token, email, cb):
        self.delete(
            "/subscribers/" + self.compress_id(id, token) + "/" + email,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )
