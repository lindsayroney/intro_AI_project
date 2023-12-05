import androidx.room.Database;
import androidx.room.RoomDatabase;

@Database(entities = {StickerData.class}, version = 1)
public abstract class StickerDatabase extends RoomDatabase {
    public abstract StickerDataDao stickerDataDao();
}
