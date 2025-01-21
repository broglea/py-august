import dateutil.parser


class Pin:
    def __init__(self, data):
        self._pin_id = data.get("_id")
        self._lock_id = data.get("lockID")
        self._user_id = data.get("userID")
        self._state = data.get("state")
        self._pin = data.get("pin")
        self._slot = data.get("slot")
        self._access_type = data.get("accessType")
        self._first_name = data.get("firstName")
        self._last_name = data.get("lastName")
        self._unverified = data.get("unverified")

        self._created_at = data.get("createdAt")
        self._updated_at = data.get("updatedAt")
        self._loaded_date = data.get("loadedDate")
        self._access_start_time = data.get("accessStartTime")
        self._access_end_time = data.get("accessEndTime")
        self._access_times = data.get("accessTimes")

    @property
    def pin_id(self):
        return self._pin_id

    @property
    def lock_id(self):
        return self._lock_id

    @property
    def user_id(self):
        return self._user_id

    @property
    def state(self):
        return self._state

    @property
    def pin(self):
        return self._pin

    @property
    def slot(self):
        return self._slot

    @property
    def access_type(self):
        return self._access_type

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def unverified(self):
        return self._unverified

    @property
    def created_at(self):
        return dateutil.parser.parse(self._created_at)

    @property
    def updated_at(self):
        return dateutil.parser.parse(self._updated_at)

    @property
    def loaded_date(self):
        return dateutil.parser.parse(self._loaded_date)

    @property
    def access_start_time(self):
        if not self._access_start_time:
            return None
        return dateutil.parser.parse(self._access_start_time)

    @property
    def access_end_time(self):
        if not self._access_end_time:
            return None
        return dateutil.parser.parse(self._access_end_time)

    @property
    def access_times(self):
        if not self._access_times:
            return None
        return dateutil.parser.parse(self._access_times)

    def __repr__(self):
        return "Pin(id={} firstName={}, lastName={})".format(
            self.pin_id,
            self.first_name,
            self.last_name,
        )
