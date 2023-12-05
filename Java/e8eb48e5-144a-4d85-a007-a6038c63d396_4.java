StickerDatabase stickerDatabase = Room.databaseBuilder(getApplicationContext(), StickerDatabase.class, "sticker_db").build();
StickerDataDao stickerDataDao = stickerDatabase.stickerDataDao();
