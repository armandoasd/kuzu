#pragma once

#include "processor/operator/copy_csv/copy_csv.h"
#include "storage/store/rels_store.h"

namespace kuzu {
namespace processor {

class CopyRelCSV : public CopyCSV {
public:
    CopyRelCSV(Catalog* catalog, CSVDescription csvDescription, table_id_t tableID, WAL* wal,
        NodesStatisticsAndDeletedIDs* nodesStatisticsAndDeletedIDs, uint32_t id,
        const string& paramsString, RelsStatistics* relsStatistics)
        : CopyCSV{PhysicalOperatorType::COPY_REL_CSV, catalog, std::move(csvDescription), tableID,
              wal, id, paramsString},
          nodesStatisticsAndDeletedIDs{nodesStatisticsAndDeletedIDs}, relsStatistics{
                                                                          relsStatistics} {}

    string execute(TaskScheduler* taskScheduler, ExecutionContext* executionContext) override;

    unique_ptr<PhysicalOperator> clone() override {
        return make_unique<CopyRelCSV>(catalog, csvDescription, tableID, wal,
            nodesStatisticsAndDeletedIDs, id, paramsString, relsStatistics);
    }

private:
    NodesStatisticsAndDeletedIDs* nodesStatisticsAndDeletedIDs;
    RelsStatistics* relsStatistics;
};

} // namespace processor
} // namespace kuzu
