import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

