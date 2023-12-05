@Transactional
public void saveEntity(Entity entity) {
    // Repository save operation
    repository.save(entity);
}
