# Test Log

## Test Session: 2026-01-21

### Add Task Feature
- ✅ Adds task with valid input
- ✅ Rejects empty input
- ✅ Saves to file correctly

### View Tasks Feature
- ✅ Shows all tasks correctly
- ✅ Shows "no tasks" when empty
- ✅ Formats dates properly

### Delete Task Feature
- ✅ Deletes existing task

## Bugs Found
1. Long input crashes - need to limit characters
2. Invalid ID causes crash - need validation

## Bugs Fixed

[//]: # (1. Added character limit &#40;500 chars&#41;)

[//]: # (2. Added ID validation in delete function)
