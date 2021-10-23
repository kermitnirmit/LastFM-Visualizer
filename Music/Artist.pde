class Artist {
    String name;
    float[] values = new float[DAY_LEN];
    int[] ranks = new int[DAY_LEN];
    int[] daysInTopTen = new int[DAY_LEN];
    int[] consecutiveDays = new int[DAY_LEN];
    color c;
    public Artist(String name) {
        this.name = name;
        for (int i = 0; i < DAY_LEN; ++i) {
            values[i] = 0;
            ranks[i] = TOP_VISIBLE + 7;
            daysInTopTen[i] = 0;
            consecutiveDays[i] = 0;
        }
        c = color(random(50, 200), random(50, 200), random(50, 200));
    }
}
