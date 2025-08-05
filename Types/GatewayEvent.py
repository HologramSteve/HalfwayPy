class GatewayEvent:
    def __init__(self, data: dict):
        self.type = data.get("t")
        self.sequence = data.get("s")
        self.opcode = data.get("op")
        self.data = data.get("d")
        self.raw = data

    def __repr__(self):
        return f"<GatewayEvent type={self.type!r} sequence={self.sequence!r} opcode={self.opcode!r} data={self.data!r}>"
