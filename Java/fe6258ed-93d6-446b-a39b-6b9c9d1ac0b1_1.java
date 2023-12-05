ObjectMapper objectMapper = new ObjectMapper();
objectMapper.addMixIn(Point.class, PointMixin.class);
