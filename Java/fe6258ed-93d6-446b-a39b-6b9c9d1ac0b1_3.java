ObjectMapper objectMapper = new ObjectMapper();
SimpleModule module = new SimpleModule();
module.addDeserializer(Point.class, new PointDeserializer());
objectMapper.registerModule(module);
