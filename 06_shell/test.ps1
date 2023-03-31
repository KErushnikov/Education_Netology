if (($args.Count -eq 1) -and (Test-Path -PathType Container -Path $args[0]))
{
    "$args - dir"
}
elseif (($args.Count -eq 1) -and (Test-Path -Path $args[0]))
{
    "$args - file"
}
else
{
    "Wrong number of arguments or inputed directory or file does not exist"
}