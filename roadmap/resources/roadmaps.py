from . import model


class Roadmap(model.Model):
    time_frames = {
        "quarters": 0,
        "sixMonths": 1,
        "yearly": 2,
        "curentSoonFuture": 3
    }

    custom_types = {
        "text": 0,
        "int": 1,
        "float": 2,
        "date": 3
    }

    meta_data_types = {
        "objectives": 0,
        "teams": 1,
        "tags": 2
    }

    def create(self, name, cb, limit_reached):
        def err_handler(err, status_code):
            if status_code is 406:
                limit_reached()
            else:
                cb(err)

        self.post(
            "/roadmaps",
            {"name": name},
            lambda result: cb(None, result),
            err_handler
        )

    def add_item(self, data, cb):
        self.post(
            "/roadmap/items",
            data,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def all(self, cb):
        self.get(
            "/roadmaps",
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def summary(self, cb):
        self.get(
            "/roadmaps/summary",
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def multi_overview(self, cb):
        self.get(
            "/roadmaps/multi",
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def get_roadmap(self, roadmap_id, cb):
        self.get(
            "/roadmaps/" + roadmap_id,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def get_item(self, roadmap_id, id, cb):
        self.get(
            "/roadmaps/" + roadmap_id + "/item/" + id,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def get_items(self, roadmap_id, type, cb):
        self.get(
            "/roadmaps/" + roadmap_id + "/items/" + type,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def get_completed(self, roadmap_id, cb):
        self.get(
            "/roadmaps/" + roadmap_id + "/completed",
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def update(self, data, cb):
        self.put(
            "/roadmaps/" + data.id,
            data,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def get_github_repos(self, id, cb):
        self.get(
            "/roadmaps/" + id + "/github/repos",
            lambda result: cb(None, result),
            lambda err: cb(err),
            True
        )

    def set_trello(self, data, cb):
        self.put(
            "/roadmaps/" + data.id + "/trello",
            data,
            lambda ok: cb(None, ok),
            lambda err: cb(err),
            True
        )

    def set_github_repo(self, id, data, cb):
        self.put(
            "/roadmaps/" + id + "/github",
            lambda ok: cb(None, ok),
            lambda err: cb(err),
            True
        )

    def set_privacy(self, id, is_private, cb):
        self.put(
            "/roadmaps/" + id + "/privacy",
            {
                "roadmapId": id,
                "private": is_private
            },
            lambda ok: cb(None, ok),
            lambda err: cb(err)
        )

    def set_domain(self, subdomain, domain, cb):
        self.put(
            "/roadmaps/" + id + "/domain",
            {
                "subDomain": subdomain,
                "domain": domain
            },
            lambda ok: cb(None, ok),
            lambda err: cb(err)
        )

    def set_options(self, data, cb):
        self.put(
            "/roadmaps/" + data.id + "/options",
            data,
            lambda ok: cb(None, ok),
            lambda err: cb(err)
        )

    def set_meta(self, roadmap_id, meta_data_type, values, cb):
        self.put(
            "/roadmaps/" + roadmap_id + "/meta",
            {
                "roadmapId": roadmap_id,
                "metaDataType": meta_data_type,
                "values": values
            },
            lambda results: cb(None, results),
            lambda err: cb(err)
        )

    def update_item(self, data, cb):
        self.put(
            "/roadmaps/" + data.roadmapId + "/items",
            data,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def delete_item(self, roadmap_id, item_id, cb):
        self.delete(
            "/roadmaps/" + roadmap_id + "/items/" + item_id,
            lambda: cb(None, None),
            lambda err: cb(err)
        )

    def del_item(self, roadmap_id, item_id, cb):
        self.delete_item(roadmap_id, item_id, cb)

    def stats(self, roadmap_id, cb):
        self.get(
            "/roadmaps/" + roadmap_id + "/stats",
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def dashboard(self, roadmap_id, cb):
        self.get(
            "/roadmaps/" + roadmap_id + "/dashboard",
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def delete_roadmap(self, id, cb):
        self.delete(
            "/roadmaps/" + id,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def update_mockup(self, roadmap_id, item_id, mockup, cb):
        self.put(
            "/roadmaps/" + roadmap_id + "/items/" + item_id + "/mockup",
            mockup,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )

    def delete_mockup(self, roadmap_id, item_id, mockup_id, cb):
        self.delete(
            "/roadmaps/" + roadmap_id + "/items/" + item_id + "/mockup/" + mockup_id,
            lambda result: cb(None, result),
            lambda err: cb(err)
        )
