#include "planner/operator/scan/logical_scan_file.h"
#include "planner/planner.h"

using namespace kuzu::binder;

namespace kuzu {
namespace planner {

std::shared_ptr<LogicalOperator> Planner::getScanFile(const binder::BoundFileScanInfo* info) {
    return std::make_shared<LogicalScanFile>(info->copy(), nullptr /* offset */);
}

void Planner::appendScanFile(const BoundFileScanInfo* info, LogicalPlan& plan) {
    appendScanFile(info, nullptr /* offset */, plan);
}

void Planner::appendScanFile(const binder::BoundFileScanInfo* info,
    std::shared_ptr<Expression> offset, LogicalPlan& plan) {
    KU_ASSERT(plan.isEmpty());
    auto scanFile = std::make_shared<LogicalScanFile>(info->copy(), offset);
    scanFile->computeFactorizedSchema();
    plan.setLastOperator(std::move(scanFile));
}

} // namespace planner
} // namespace kuzu
