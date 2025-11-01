import json

class Defs(object):
    def sum_pixels(self, pixels): 
        total_r = total_g = total_b = total_count = 0
        for count, (r, g, b) in pixels:
            total_r += r * count
            total_g += g * count
            total_b += b * count
            total_count += count

        total_color = (total_r, total_g, total_b)
        avg_color = (total_r // total_count, total_g // total_count, total_b // total_count)

        return {"sum": total_color,"average": avg_color,"count": total_count}
    
    def get_json(self, path):
        with open(path, "r+") as cfg:
            return json.load(cfg)
