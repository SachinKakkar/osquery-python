import os
import osquery
import pytest

def test_spawn_and_query_osquery_info():
    """Test that osqueryd can be spawned and queried via SpawnInstance."""

    instance = osquery.SpawnInstance()
    instance.open()

    try:
        result = instance.client.query("SELECT version, build_platform FROM osquery_info;")
        rows = result.response

        assert isinstance(rows, list), "Query response is not a list"
        assert len(rows) > 0, "No rows returned"
        assert "version" in rows[0], "Missing 'version' column"
        assert "build_platform" in rows[0], "Missing 'build_platform' column"
    finally:
         # instance._proc.terminate()
         print ("done")
