#ifndef MERCATOR_UTIL_CONFIG_H_
#define MERCATOR_UTIL_CONFIG_H_

#include <boost/program_options.hpp>
#include <string>

namespace mercator {

class ConfigManager {
 public:
  ConfigManager(); 

  bool ReadConfigFile(const std::string&);

  const std::string PrintOptions() const;

  double uncertainty_threshold;
  double camera_pixel_size;
  double min_ground_sampling_distance;
  uint64_t min_cameras;
  short print_ba_summary;

 private:
  boost::program_options::options_description desc_;
  boost::program_options::variables_map vmap_;

};

} // namespace mercator

#endif // MERCATOR_UTIL_CONFIG_H_
