List<String> list = strings.stream().collect(Collectors.toList());

String joined = strings.stream().collect(Collectors.joining(", "));
