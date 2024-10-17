
local arr = std.makeArray(25, function(x) "MKBO-" + (x + 1) + "-24");

local Person(age, group, name) = {
  age: age,
  group: arr[group - 1],
  name: name,
};

{
  groups: arr,
  students: [
    Person(19, 4, ''),
    Person(18, 5, ''),
    Person(18, 5, ''),
    Person(19, 11, ''),
  ],
  subject: "",
}
```
