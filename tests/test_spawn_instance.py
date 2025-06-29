import os
import osquery
import pytest

def test_spawn_and_query_osquery_info():
    """Test that osqueryd can be spawned and queried via SpawnInstance."""

    osqueryd_path = "/Users/sachinkakkar/bin/osqueryd"  # ← Update this if needed
    assert os.path.exists(osqueryd_path), f"osqueryd not found at {osqueryd_path}"

    instance = osquery.SpawnInstance()
    instance.set_osqueryd_path(osqueryd_path)
    instance.open()

    try:
        result = instance.client.query("SELECT version, build_platform FROM osquery_info;")
        rows = result.response

        assert isinstance(rows, list), "Query response is not a list"
        assert len(rows) > 0, "No rows returned"
        assert "version" in rows[0], "Missing 'version' column"
        assert "build_platform" in rows[0], "Missing 'build_platform' column"
    finally:
        # instance.close()
        if hasattr(instance, "_proc") and instance._proc:
            instance._proc.terminate()
            instance._proc.wait(timeout=5)
