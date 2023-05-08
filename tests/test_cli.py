from pytest_console_scripts import ScriptRunner


def test_hello_world(script_runner: ScriptRunner) -> None:
    args = ["stac", "hello"]
    result = script_runner.run(*args)
    assert result.success
    assert result.stdout == "Hello World!\n"
    assert result.stderr == ""
